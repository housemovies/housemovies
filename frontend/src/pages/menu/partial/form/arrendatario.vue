<template>
  <l-card titulo="Arrendatario">
    <template slot="acciones">
      <div class="col-10">
        <l-select-api
          col="8"
          class_val=""
          v-model="value.arrendatario_id"
          emit-value
          map-options
          option-value="id"
          option-label="n_completo"
          label="Buscar Arrendatario"
          url="tercero/arrendatarios/select/"
        />
      </div>
    </template>
    <l-select-api
      col="4"
      v-model="value.arrendatario.persona.regimen_tributario_id"
      option-value="id"
      option-label="nombre"
      url="tercero/regimen/select"
      label="Regimen *"
      :rules="[$rules.required($t('validator.required'))]"
    />
    <l-tipo-documento
      col="4"
      :tipo_persona="6"
      v-model="value.arrendatario.persona.tipo_documento_id"
      label="tipo_documento *"
      :rules="[$rules.required($t('validator.required'))]"
    />
    <l-input col="4"
             v-model="value.arrendatario.persona.documento"
             label="Documento *"
             :rules="[$rules.required($t('validator.required'))]"
    />
    <l-input col="6"
             v-model="value.arrendatario.persona.p_nombre"
             label="Primer Nombre *"
             :rules="[$rules.required($t('validator.required'))]"
    />
    <l-input col="6"
             v-model="value.arrendatario.persona.s_nombre"
             label="Segundo Nombre"
    />
    <l-input col="6"
             v-model="value.arrendatario.persona.p_apellido"
             label="Primer Apellido *"
             :rules="[$rules.required($t('validator.required'))]"
    />
    <l-input col="6"
             v-model="value.arrendatario.persona.s_apellido"
             label="Segundo Apellido"
    />
    <l-input col="12"
             v-model="value.arrendatario.persona.n_completo"
             label="Nombre Completo o Razón Social"
    />
    <!-- <l-input
      col="12"
      v-model="value.arrendatario.persona.email"
      label="Correo *"
      :rules="[
        $rules.email($t('validator.email')),
        $rules.required($t('validator.required'))
      ]"
    /> -->
  </l-card>
</template>

<script>
export default {
  name: 'SolicitudFormDeudores',
  props: {
    value: {
      type: Object
    }
  },
  watch: {
    'value.arrendatario.persona.p_nombre' (val) {
      const snombre = this.value.arrendatario.persona.s_nombre || ''
      const papellido = this.value.arrendatario.persona.p_apellido || ''
      const sapellido = this.value.arrendatario.persona.s_apellido || ''
      this.value.arrendatario.persona.n_completo = `${val || ''} ${snombre} ${papellido} ${sapellido}`
    },
    'value.arrendatario.persona.s_nombre' (val) {
      const pnombre = this.value.arrendatario.persona.p_nombre || ''
      const papellido = this.value.arrendatario.persona.p_apellido || ''
      const sapellido = this.value.arrendatario.persona.s_apellido || ''
      this.value.arrendatario.persona.n_completo = `${pnombre} ${val || ''} ${papellido} ${sapellido}`
    },
    'value.arrendatario.persona.p_apellido' (val) {
      const pnombre = this.value.arrendatario.persona.p_nombre || ''
      const snombre = this.value.arrendatario.persona.s_nombre || ''
      const sapellido = this.value.arrendatario.persona.s_apellido || ''
      this.value.arrendatario.persona.n_completo = `${pnombre} ${snombre} ${val || ''} ${sapellido}`
    },
    'value.arrendatario.persona.s_apellido' (val) {
      const pnombre = this.value.arrendatario.persona.p_nombre || ''
      const snombre = this.value.arrendatario.persona.s_nombre || ''
      const papellido = this.value.arrendatario.persona.p_apellido || ''
      this.value.arrendatario.persona.n_completo = `${pnombre} ${snombre} ${papellido} ${val || ''}`
    },
    async 'value.arrendatario_id' (val) {
      if (!['', null, undefined].includes(val)) {
        this.value.arrendatario = await this.Get(`tercero/arrendatarios/${val}`)
      } else {
        this.value.arrendatario = {
          telefonos_tipos_personas: [],
          direcciones_tipos_personas: [],
          persona: {}
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
