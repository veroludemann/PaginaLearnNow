const { createApp } = Vue

createApp({
  data() {
    return {
      novedades: []
    }
  },
  methods: {
    fetchData(url) {

        fetch(url)
            .then(response => response.json())
            .then(data => { 
                this.novedades=data.novedades  // guarda en  array drinks  obtenido del json dl a tributo drikk
                console.log(this.novedades)
            })

    }
  },
  created(){

    this.fetchData("https://veroludemann.github.io/miJson/info.json") 
  }

}).mount('#app')