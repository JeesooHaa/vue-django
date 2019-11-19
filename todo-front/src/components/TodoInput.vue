<template>
  <div class="todo-input">
    <!-- prevent 실제 요청이 없도록... -->
    <form class="input-group mb-3" @submit.prevent="onSubmit">
      <input v-model="title" type="text" class="form-control">
      <button type="submit" class="btn btn-success">add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: ''
    }
  },
  methods: {
    onSubmit() {
      this.$emit('createTodo', this.title)
      this.title = ''
    }
  }
}
</script>

<style>

</style>