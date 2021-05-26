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
            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/dashboard" class="button is-light">Dashboard</router-link>
                <router-link to="/dashboard/clients" class="button is-light">Clients</router-link>
                <router-link to="/dashboard/invoices" class="button is-light">Invoices</router-link>
                <router-link to="/dashboard/my-account" class="button is-light">MyAccount</router-link>
              </div>
            </div>
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
