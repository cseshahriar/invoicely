<template>
    <div class="page-myaccount">
        <div class="columns">
            <div class="column is-8 is-offset-2">
                <h1>My Account</h1>
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: 'MyAccount',
    methods: {
        logout() {
            axios
            .post("/api/v1/token/logout/")
            .then(response => {
                axios.defaults.headers.common['Authorization'] = ""
                localStorage.removeItem('token')
                this.$store.commit('removeToken')
                this.$router.push('/')
            })
            .catch(error => {
                if(error.response) {
                    console.log(JSON.stringify(error.response.data))
                } else if( error.message) {
                    console.log(JSON.stringify(error.message))
                } else {
                    console.log(JSON.stringify(error))
                }
            })
        }
    }
    
}
</script>