<template>
  <q-form ref="FormDeudor" >
    <l-card titulo="Deudor Solidario">
      <template slot="acciones">
        <div class="col-8">
          <l-select-api
            col="12"
            v-model="value.deudor_id"
            emit-value
            map-options
            option-value="id"
            option-label="n_completo"
            label="Buscar Deudor Solidario"
            url="tercero/deudores/select/"
          />
        </div>
        <div class="col-1">
          <q-btn flat round dense icon="save_alt" @click="agregarDeudor">
             <q-tooltip content-style="font-size: 16px" :offset="[10, 10]">
                Agregar Deudor
              </q-tooltip>
          </q-btn>
        </div>
      </template>
        <l-select-api
          col="4"
          v-model="value.deudor.persona.regimen_tributario_id"
          option-value="id"
          option-label="nombre"
          url="tercero/regimen/select"
          label="Regimen *"
          :rules="[$rules.required($t('validator.required'))]"
        />
        <l-tipo-documento
          col="4"
          :tipo_persona="6"
          v-model="value.deudor.persona.tipo_documento_id"
          label="tipo_documento *"
          :rules="[$rules.required($t('validator.required'))]"
        />
        <l-input col="4"
                v-model="value.deudor.persona.documento"
                label="Documento *"
                :rules="[$rules.required($t('validator.required'))]"
        />
        <l-input col="6"
                v-model="value.deudor.persona.p_nombre"
                label="Primer Nombre *"
                :rules="[$rules.required($t('validator.required'))]"
        />
        <l-input col="6"
                v-model="value.deudor.persona.s_nombre"
                label="Segundo Nombre"
        />
        <l-input col="6"
                v-model="value.deudor.persona.p_apellido"
                label="Primer Apellido *"
                :rules="[$rules.required($t('validator.required'))]"
        />
        <l-input col="6"
                v-model="value.deudor.persona.s_apellido"
                label="Segundo Apellido"
        />
        <l-input col="12"
                v-model="value.deudor.persona.n_completo"
                label="Nombre Completo o Razón Social"
        />
        <!-- <l-input
          col="12"
          v-model="value.deudor.persona.email"
          label="Correo *"
          :rules="[
            $rules.email($t('validator.email')),
            $rules.required($t('validator.required'))
          ]"
        /> -->
    </l-card>
  </q-form>
</template>

<script>
export default {
  name: 'SolicitudFormdeudor',
  props: {
    value: {
      type: Object
    }
  },
  watch: {
    'value.deudor.persona.p_nombre' (val) {
      const snombre = this.value.deudor.persona.s_nombre || ''
      const papellido = this.value.deudor.persona.p_apellido || ''
      const sapellido = this.value.deudor.persona.s_apellido || ''
      this.value.deudor.persona.n_completo = `${val || ''} ${snombre} ${papellido} ${sapellido}`
    },
    'value.deudor.persona.s_nombre' (val) {
      const pnombre = this.value.deudor.persona.p_nombre || ''
      const papellido = this.value.deudor.persona.p_apellido || ''
      const sapellido = this.value.deudor.persona.s_apellido || ''
      this.value.deudor.persona.n_completo = `${pnombre} ${val || ''} ${papellido} ${sapellido}`
    },
    'value.deudor.persona.p_apellido' (val) {
      const pnombre = this.value.deudor.persona.p_nombre || ''
      const snombre = this.value.deudor.persona.s_nombre || ''
      const sapellido = this.value.deudor.persona.s_apellido || ''
      this.value.deudor.persona.n_completo = `${pnombre} ${snombre} ${val || ''} ${sapellido}`
    },
    'value.deudor.persona.s_apellido' (val) {
      const pnombre = this.value.deudor.persona.p_nombre || ''
      const snombre = this.value.deudor.persona.s_nombre || ''
      const papellido = this.value.deudor.persona.p_apellido || ''
      this.value.deudor.persona.n_completo = `${pnombre} ${snombre} ${papellido} ${val || ''}`
    },
    async 'value.deudor_id' (val) {
      if (!['', null, undefined].includes(val)) {
        this.value.deudor = await this.Get(`tercero/deudores/${val}`)
      } else {
        this.value.deudor = {
          telefonos_tipos_personas: [],
          direcciones_tipos_personas: [],
          persona: {}
        }
      }
    }
  },
  methods: {
    async agregarDeudor () {
      try {
        const validate = await this.$refs.FormDeudor.validate()
        if (validate) {
          this.value.deudores.push(this.value.deudor.persona)
          this.value.deudor.persona = {}
        }
      } catch ({ message }) {
        console.error(message)
      }
    }
  }
}
</script>

<style scoped>

</style>
