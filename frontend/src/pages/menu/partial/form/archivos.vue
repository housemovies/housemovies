<template>
  <l-card titulo="Archivos" col="2">
    <template slot="acciones">
      <q-space/>
      <q-file
        v-model="files"
        borderless
        input-class="invisible"
        @input="preview"
        accept=".pdf"
        style="width: 50px;height: 50px">
         <div class="text-white" style="font-size: 2em">
            <q-icon name="backup" />
         </div>
      </q-file>
    </template>
    <div class="col-12" >
      <q-list dense >
        <q-item  v-for="(item, index) in value" :name="index" :key="index" >
          <q-item-section class="col-11 text-subtitle2 text-left">
             <router-link :to="{ hash: '#Handling-links', query: { search: '1', test: '1' } }">
                {{ item.src.name }}
            </router-link>
          </q-item-section>
          <q-item-section class="col-1 text-subtitle2 text-left">
            <q-btn flat round dense icon="delete_forever" @click="quitarArchivo(index)">
              <q-tooltip content-style="font-size: 16px" :offset="[10, 10]">
                Eliminar Archivo
              </q-tooltip>
          </q-btn>
          </q-item-section>
        </q-item>
      </q-list>
    </div>
    <!-- <div class="col-12">
      <q-carousel
        swipeable
        animated
        v-model="slide"
        thumbnails
        infinite
      >
        <q-carousel-slide v-for="(item, index) in value"
          :name="index" :key="index"
          :img-src="item.url"/>
      </q-carousel>
    </div> -->
  </l-card>
</template>

<script>
// limite 2 Mb de peso
import { mapGetters } from 'vuex'
export default {
  name: 'SolicitudFormArchivos',
  props: {
    value: {
      type: Array
    }
  },
  data () {
    return {
      slide: 1,
      files: null
    }
  },
  computed: {
    ...mapGetters('auth', ['token'])
  },
  methods: {
    preview (file) {
      const temp = [...this.value]
      console.log(file)
      temp.push({ src: file, url: URL.createObjectURL(file) })
      this.$emit('input', temp)
    },
    quitarArchivo (index) {

    },
    factoryFn (file) {
      return new Promise((resolve, reject) => {
        resolve({
          url: '/api/inmueble/inmuebles/upload-temp/',
          method: 'POST',
          headers: [
            { name: 'Authorization', value: `Token ${this.token}` }
          ]
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
