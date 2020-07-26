<template>
<q-page padding>
  <q-stepper
    v-model="step"
    header-nav
    ref="stepper"
    color="primary"
    animated
  >
    <q-step
      :name="1"
      title="Creacion de Inmueble"
      caption="Información General"
      icon="settings"
      :done="step > 1"
      :header-nav="step > 1"
    >
      <div class="q-pa-md q-gutter-sm">
        <q-banner rounded class="bg-grey-3">
          <q-form
            @submit="onSubmit"
            ref="FormInmueble"
            class="q-pa-md q-gutter-md "
          >
            <component :is="`form-formulario`" v-model="model"/>
            <div class="row justify-end">
              <l-bottom
                icono="save"
                label="Siguiente"
                color="primary"
                class_val=" "
                :outline="false"
                :rounded="false"
              />
            </div>
          </q-form>
        </q-banner>
      </div>
    </q-step>
    <q-step
      :name="2"
      title="Asignación Propietarios"
      icon="group"
      :done="step > 2"
      :header-nav="step > 2"
    >
      <div class="q-pa-md q-gutter-sm">
        <q-banner rounded class="bg-grey-3">
          <div class="q-pa-md q-gutter-md ">
            <component :is="'form-asignar-propietarios'" v-model="model"/>
            <div class="row justify-end">
              <q-btn-group>
                <l-bottom
                  @click="step = 1"
                  icono="undo"
                  label="Anterior"
                  color="white"
                  class_val="text-black"
                  :outline="false"
                  :rounded="false"
                  type=" "
                />
                <l-bottom
                  @click="step = 3"
                  icono="redo"
                  label="Siguiente"
                  color="primary"
                  class_val=" "
                  :outline="false"
                  :rounded="false"
                  type=" "
                />
              </q-btn-group>
            </div>
          </div>
        </q-banner>
      </div>
    </q-step>
    <q-step
      :name="3"
      title="Caracteristicas"
      icon="ballot"
      :done="step > 3"
      :header-nav="step > 3"
    >
      <div class="q-pa-md q-gutter-sm">
        <q-banner rounded class="bg-grey-3">
          <div class="q-pa-md q-gutter-md ">
            <component :is="'form-asignar-caracteristicas'" v-model="model"/>
            <div class="row justify-end">
              <q-btn-group>
                <l-bottom
                  @click="step = 2"
                  icono="undo"
                  label="Anterior"
                  color="white"
                  class_val="text-black"
                  :outline="false"
                  :rounded="false"
                  type=" "
                />
                <l-bottom
                  @click="step = 4"
                  icono="redo"
                  label="Siguiente"
                  color="primary"
                  class_val=" "
                  :outline="false"
                  :rounded="false"
                  type=" "
                />
              </q-btn-group>
            </div>
          </div>
        </q-banner>
      </div>
    </q-step>
    <q-step
      :name="4"
      title="Imagenes"
      icon="camera_alt"
    >
      <div class="q-pa-md q-gutter-sm">
        <q-banner rounded class="bg-grey-3">
          <div class="q-pa-md q-gutter-md ">
            <!-- <div class="q-pa-md"> -->
              <q-uploader
                ref="upload"
                :url="`/api/inmueble/inmuebles/${this.id}/upload/`"
                style="width: 98.5%"
                label="Carga Archivos"
                multiple
                field-name="src"
                :headers="[
                  {name: 'Authorization', value: `Token ${token}`}
                ]"
              />
            <!-- </div> -->
            <!-- <div class="q-pa-md"> -->
              <q-carousel
                swipeable
                animated
                v-model="slide"
                thumbnails
                infinite
              >
                <q-carousel-slide v-for="(archivo, index) in model.archivos" :key="archivo.src" :name="index" img-src="/api/media/bita_archivos/processed_r53PpNc.jpeg" />
              </q-carousel>
            <!-- </div> -->
            <div class="row justify-end">
              <q-btn-group>
                <l-bottom
                  @click="step = 2"
                  icono="undo"
                  label="Anterior"
                  color="white"
                  class_val="text-black"
                  :outline="false"
                  :rounded="false"
                  type=" "
                />
                <l-bottom
                  @click="finalizar"
                  icono="save"
                  label="Finalizar"
                  color="primary"
                  class_val=" "
                  :outline="false"
                  :rounded="false"
                  type=" "
                />
              </q-btn-group>
            </div>
          </div>
        </q-banner>
      </div>
    </q-step>
  </q-stepper>
</q-page>
</template>

<script>
import FormFormulario from './form/formulario'
import FormAsignarPropietarios from './form/asignarPropietarios'
import FormAsignarCaracteristicas from './form/asignarCaracteristicas'
import { mapActions, mapGetters } from 'vuex'
export default {
  layout: 'main',
  name: 'editar',
  components: { FormFormulario, FormAsignarPropietarios, FormAsignarCaracteristicas },
  props: {
    id: {
      type: String,
      default: '0'
    }
  },
  data () {
    return {
      model: {
        administracion_inmueble: {
          valor: 0
        },
        propietarios: [],
        caracteristicas: []
      },
      destinos: [],
      usos: [],
      tiposinmuebles: [],
      tiposadministraciones: [],
      ciudades: [],
      step: 1,
      slide: 1
    }
  },
  computed: {
    ...mapGetters('auth', ['token'])
  },
  mounted () {
    this.getLoad()
  },
  methods: {
    ...mapActions('http', ['Get', 'Post', 'Put']),
    /* async getRecursos () {
      try {
        this.destinos = await this.Get({ api: 'inmueble/destinos' })
        this.ciudades = await this.Get({ api: 'ubicacion/ciudades' })
        this.usos = await this.Get({ api: 'inmueble/usos' })
        this.tiposinmuebles = await this.Get({ api: 'inmueble/tipoinmuebles' })
        this.tiposadministraciones = await this.Get({ api: 'inmueble/tipoadministracion' })
        this.getLoad()
      } catch ({ message }) {
        console.error(message)
      }
    }, */
    async getLoad () {
      try {
        this.model = await this.Get({ api: 'inmueble/inmuebles/' + this.id })
      } catch ({ message }) {
        console.error(message)
      }
    },
    async onSubmit () {
      try {
        const validate = await this.$refs.FormInmueble.validate()
        if (validate) {
          const data = await this.Put({ api: 'inmueble/inmuebles/' + this.id, model: this.model })
          this.model.id = data.id
          this.step = 2
          this.$emit('save', data)
        }
      } catch ({ message }) {
        console.error(message)
      }
    },
    finalizar () {
      const $route = this.$router
      this.LConfim('Exito!',
        'Proceso terminado exitosamente!',
        () => { $route.replace({ name: 'InmueblesAdministrar' }) }
      )
    }
  }
}
</script>

<style scoped>

</style>
