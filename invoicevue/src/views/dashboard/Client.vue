<template>
    <div class="page-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{client.name}}</h1>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: 'Client',
    data() {
        return {
            client: {}
        }
    },
    mounted() {
        this.getClient()
    },
    methods: {
        getClient() {
            
            const clientID = this.$route.params.id

            axios
                .get(`/api/v1/clients/${clientID}`)
                .then(response => {
                    this.client = response.data
                })
                .catch(error => {
                    console.error(error)
                })
        }
    }
}
</script>
