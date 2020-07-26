<template>
  <q-page padding>
    <q-form
      @submit="onSubmit"
      ref="FormInmueble"
    >
      <div class="row ">
        <div class="col-xs-12 col-sm-12 q-pa-sm q-gutter-y-md">
          <solicitud-form-general v-model="inmueble"/>
        </div>
        <div class="col-xs-12 col-sm-6 q-pa-sm q-gutter-y-md">
          <solicitud-form-arrendatario v-model="model"/>
        </div>
        <div class="col-xs-12 col-sm-6 q-pa-sm q-gutter-y-md">
          <solicitud-form-deudor v-model="model"/>
        </div>
        <div class="col-xs-12 col-sm-6 q-pa-sm q-gutter-y-md">
          <solicitud-form-archivos v-model="archivos"/>
        </div>
        <div class="col-xs-12 col-sm-6 q-pa-sm q-gutter-y-md">
          <listado-deudores v-model="model"/>
        </div>
      </div>
    </q-form>
    <q-page-sticky position="top-right" :offset="[18, 5]" >
      <q-btn fab icon="send" color="accent" style="z-index: 99999"/>
    </q-page-sticky>
  </q-page>
</template>

<script>
import SolicitudFormGeneral from 'pages/solicitud/partial/form/general'
import SolicitudFormArrendatario from 'pages/solicitud/partial/form/arrendatario'
import SolicitudFormDeudor from 'pages/solicitud/partial/form/deudor'
import listadoDeudores from 'pages/solicitud/partial/form/listadodeudores'
import solicitudFormArchivos from 'pages/solicitud/partial/form/archivos'
export default {
  layout: 'main',
  name: 'crear',
  components: {
    SolicitudFormGeneral,
    SolicitudFormArrendatario,
    SolicitudFormDeudor,
    listadoDeudores,
    solicitudFormArchivos
  },
  
  data () {
    return {
      inmueble: {},
      model: {
        consignacion: {},
        barrio: {},
        arrendatario: {
          telefonos_tipos_personas: [],
          direcciones_tipos_personas: [],
          persona: {}
        },
        deudor: {
          telefonos_tipos_personas: [],
          direcciones_tipos_personas: [],
          persona: {}
        },
        deudores: []
      },
      archivos: []
    }
  },
  mounted () {
    this.getLoad()
  },
  methods: {
    async getLoad () {
      try {
        this.inmueble = await this.Get('inmueble/inmuebles/' + this.id)
      } catch ({ message }) {
        console.error(message)
      }
    },
    async onSubmit () {
      try {
        const validate = await this.$refs.FormInmueble.validate()
        if (validate) {
          const data = await this.Post('inmueble/inmuebles', this.model)
          // this.model.id = data.id
          // this.step = 2
          this.$emit('save', data)
        }
      } catch ({ message }) {
        console.error(message)
      }
    },
    finalizar () {
      const $router = this.$router
      this.LConfim('Exito!',
        'Proceso terminado exitosamente!',
        () => {
          $router.replace({ name: 'InmueblesAdministrar' })
        }
      )
    }
  }
}
</script>
