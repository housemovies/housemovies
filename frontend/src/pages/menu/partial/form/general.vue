<template>
  <l-card titulo="Creación de Solicitud">
    <l-input col="6"
      v-model="value.direccion"
      label="Dirección"
      disable
    />
    <l-input col="2"
      v-model="value.ciudad"
      label="Ciudad"
      disable
      :rules="[true]"
    />
    <l-input col="2"
      v-model="value.barrio.zonas"
      label="Zona"
      disable
    />
    <l-input col="2"
      v-model="value.barrio.nombre"
      label="Barrio"
      disable
    />
    <l-money col="2"
      v-model="value.canon"
      label="Canon"
      :rules="[true]"
      disable
    />
    <l-money col="2"
      v-model="value.admon"
      label="Admon"
      :rules="[true]"
      disable
    />
    <l-money col="2"
      v-model="value.iva_arriendo"
      label="Iva Arriendo"
      :rules="[true]"
      disable
    />
    <l-money col="2"
      v-model="Ctotal"
      label="Total"
      :rules="[true]"
      disable
    />
    <l-select-api
          col="4"
          class_val=""
          v-model="value.afianzadora_id"
          emit-value
          map-options
          option-value="id"
          option-label="n_completo"
          label="Afianzadora"
          url="tercero/afianzadoras/select/"
        />
  </l-card>
</template>
<script>
export default {
  name: 'SolicitudFormGeneral',
  props: {
    value: {
      type: Object
    }
  },
  data () {
    return {
      total: 0
    }
  },
  computed: {
    Ctotal () {
      const temp = this.value.canon + this.value.admon + this.value.iva_arriendo
      return temp
    }
  }
}
</script>

<style scoped>

</style>
