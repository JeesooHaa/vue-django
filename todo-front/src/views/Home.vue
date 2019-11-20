<template>
  <div class="home">
    <h1>Todo</h1>
    <TodoInput @createTodo="createTodo" />
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import axios from 'axios'
// import jwtDecode from 'jwt-decode' // JWT 의 payload 값을 해석해주는 라이브러리 
import { mapGetters } from 'vuex' // import vuex from 'vuex' ; vuex.mapGetters
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'
import router from '@/router'

export default {
  name: 'Home',
  data() {
    return {
      todos: []
    }
  },
  computed: {
    // ...A ; A 가 가진 아이템 다 뿌려 / js 문법 
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ]) 
  },
  components: {
    TodoList,
    TodoInput,
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다. 
    checkLoggedIn() {
      // // 1. 세션을 시작해서 
      // this.$session.start()
      // // 2. 'jwt' 가 있는지 확인하겠다. 
      // if(!this.$session.has('jwt')) {
      //   // 로그인 페이지로 보내겠다. 
      //   router.push('/login')
      // }
      if(!this.isLoggedIn) {
        router.push('/login')
      }
    },
    // 우리가 만든 django API 서버로 todos 를 달라는 요청을 보낸 뒤
    // todos data 에 할당하는 함수 
    getTodo() {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const userId = jwtDecode(token).user_id
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      // const options = {
      //   headers: {
      //     // JWT 띄어쓰기 해주세요 
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // jwt header 에 토큰 정보 없으면 에러 뜸 401
      axios.get(SERVER_IP + `/api/v1/users/${this.userId}/`, this.options)
        .then(response => {
          this.todos = response.data.todo_set
        })
        .catch(error => {
          console.log(error)
        })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      // const userId = jwtDecode(token).user_id
      // const options = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      const data = {
        title, 
        user: this.userId
      }
      axios.post(`${SERVER_IP}/api/v1/todos/`, data, this.options)
        .then(response => {
          this.todos.push(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    } 
  },
  // Vue 가 화면에 그려지면 실행하는 함수 
  // session key 삭제하고 실행하면 바로 로그인 화면으로 !!
  // null 값이 계속 반영되서 새로고침하면 로그아웃됨 
  // 일단 해결을 하기는 했는데...
  mounted() {
    if(this.isLoggedIn) {
      this.checkLoggedIn()
      this.getTodo()
    }
  },
  watch: {
    isLoggedIn() {
      this.checkLoggedIn()
      this.getTodo()      
    }
  }
}
</script>

<style>

</style>