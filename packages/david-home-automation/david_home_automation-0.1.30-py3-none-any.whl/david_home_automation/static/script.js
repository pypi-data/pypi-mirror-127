(function() {
    var app = new Vue({
        el: '#app',
        data() {
            return {
                config: {},
                defaultTemperatures: [5, 20, 25],
                responseMessage: null,
                responseBody: null
            }
        },
        async mounted() {
            this.config = (await axios.get('/api/config')).data;
            // https://stackoverflow.com/a/55379279
            this.config.thermostats.forEach(t => this.$set(t, 'temperature', 24));
        },
        methods: {
            wakeupHost: function(name) {
                this.postRequest('/api/wake-on-lan', {name});
            },
            changeToAutomatic: (name) => {
                this.postRequest('/api/thermostats/change-to-automatic', {name});
            },
            enableBoost: (name) => {
                this.postRequest('/api/thermostats/set-boost', {name});
            },
            changeTemperatureTo: function(name, temperature) {
                this.postRequest('/api/thermostats/change-temperature', {name, temperature});
            },
            postRequest: function(url, body) {
                console.log(this, url, body)
              return axios
                  .post(url, body)
                  .then((response) => {
                    this.setDebugInfo(`code ${response.status}`, response)
                  })
                  .catch((error) => {
                    this.setDebugInfo(error.message, error.response);
                  })
            },
            setDebugInfo: function(title, body) {
                this.responseMessage = title;
                this.responseBody = JSON.stringify(body, null, "\t");
            }
        }
    });
})();