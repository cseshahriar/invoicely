<template>
  <div class="wrapper">

    <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">

        <router-link to="/" class="navbar-item">Invoicely</router-link>

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
        </div>

        <div class="navbar-end">
          
          <template v-if="$store.state.isAuthenticated">
              <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>
              <router-link to="/log-out" class="button is-danger">Log Out</router-link>
          </template>

          <template v-else>
              <router-link to="/" class="navbar-item">Home</router-link>

              <div class="navbar-item">
                <div class="buttons">
                  <router-link to="/sign-up" class="button is-success">Sign Up</router-link>
                  <router-link to="/log-in" class="button is-light">Log In</router-link>
                </div>
              </div>
          </template>

        </div>
      </div>
    </nav>      

    <section class="section">
      <router-view/>
    </section>

    <footer>
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreated() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token

    if(token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = "" 
    }
  }
}
</script>

<style>
@import '../node_modules/bulma';
</style>
