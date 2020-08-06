<template>
  <div >
    <!-- <div class="q-video" style="height: 500px;">
      <iframe src="https://embed.mystream.to/e6jtjwceqbux" scrolling="no" frameborder="0" width="700" height="430" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>
    </div> -->
    <q-tab-panels v-model="tab2" animated >
      <q-tab-panel class="q-pa-none" :name="item.servidor" v-for="(item, key) in pelicula.sp_pelicula" :key="key" >
        <div class="q-video" style="height: 500px;">
          <iframe :src="item.link" scrolling="no" frameborder="0" width="700" height="430" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>
        </div>  
      </q-tab-panel>
    </q-tab-panels>
    <q-tabs
      v-model="tab2"
      indicator-color="yellow"
      class="bg-yellow-12 text-black shadow-2"
    >
      <q-tab :name="item.servidor" icon="videocam" :label="item.servidor" v-for="(item, key) in pelicula.sp_pelicula" :key="key" />     
    </q-tabs>
    <div>
      <div class="col-12">
        <div class="q-pa-md">
          <q-markup-table flat bordered>
            <thead >
              <tr>
                <th rowspan="4" style="width: 200px;">
                  <q-img
                    style="width: 165px;height: 230px"
                    :ratio="1"
                    class="rounded-borders"
                    :src="pelicula.imagen"
                  />
                </th>
                <th class="text-left text-h3" style="padding: 10px 6px !important;">   
                  <div class="row">
                    <div class="titu col-8 text-h4">
                      {{pelicula.titulo}}
                    </div>
                    <div class="col-4 text-subtitle2">
                      <q-btn clickable  outline rounded  color="black" size="md" label="Triller" style="margin-left: 5px;"  type="a" target="_blank" :href="pelicula.triller" />
                    </div>
                    <div v-if="pelicula.subtitulo" class="col-12 text-subtitle2">
                      {{pelicula.subtitulo}}
                    </div>
                    <div class="col-12 text-subtitle2">
                      Año: {{pelicula.año}} - Duración: {{pelicula.duracion}}
                    </div>
                  </div>
                </th>
              </tr>
              <tr>
                <th class="text-left" style="padding: 5px 6px !important;">
                   <div>
                    Generos:
                    <q-btn v-for="(item, key) in pelicula.mp_pelicula" :key="key" clickable  outline rounded  color="black" size="sm" :label="item.menu.nombre" style="margin-left: 5px;"  @click="redirigir(item)" />
                  </div>
                </th>
              </tr>
              <tr>
                <th class="text-left" style="padding: 5px 6px !important;">
                  <div>
                    Compartir: aca ban las redes sociales
                  </div>
                </th>
              </tr>     
               <tr>
                <th class="text-left" style="padding: 5px 6px !important;">
                </th>
              </tr>               
            </thead>
          </q-markup-table>
        </div>
      </div>
      <q-splitter
        v-model="splitterModel"
        style="height: 220px"
      >
        <template v-slot:before>
          <q-tabs
            v-model="tab"
            vertical
            class="text-white"
          >
            <q-tab name="sinopsis" icon="text_snippet" label="Sinópsis" />
            <q-tab name="reparto" icon="supervisor_account" label="Reparto" />
            <!-- <q-tab name="descargas" icon="cloud_download" label="Descargas" /> -->
          </q-tabs>
        </template>

        <template v-slot:after>
          <q-tab-panels
            v-model="tab"
            animated
            swipeable
            vertical
            transition-prev="jump-up"
            transition-next="jump-up"
          >
            <q-tab-panel name="sinopsis">
              <div class="text-h4 q-mb-md">Sinópsis</div>
              <p>
                {{pelicula.sinopsis}}
              </p>
            </q-tab-panel>

            <q-tab-panel name="reparto">
              <div class="text-h4 q-mb-md">Reparto</div>
              <p>
                {{pelicula.reparto}}
              </p>
            </q-tab-panel>

            <!-- <q-tab-panel name="descargas">
              <div class="text-h4 q-mb-md">Descargas</div>
              <p>Lorem ipsum dolor sit, amet consectetur adipisicing e.</p>
             </q-tab-panel> -->
          </q-tab-panels>
        </template>

      </q-splitter>
    </div>

  </div>
</template>

<script>
export default {
  name: 'pelicula',
  layout: 'peliculamain',
  data () {
    return { 
      pelicula: {},
      tab: 'sinopsis',
      splitterModel: 20,
      tab2: ''
    }
  },
  props: {
    id: {
      type: String,
      default: null
    }
  },
  mounted () {
    this.getPelicula()
  },
  methods: {
    async getPelicula () {
      try {
        this.pelicula = await this.Get('principal/pelicula/' + this.id)
        this.tab2 = this.pelicula.sp_pelicula[0].servidor
      } catch ({ message }) {
        console.error(message)
      }
    },
    redirigir (item) {
      this.$router.push({ name: item.menu.ruta, params: { id: (item.menu.id).toString() } })
    }
  }
}
</script>
