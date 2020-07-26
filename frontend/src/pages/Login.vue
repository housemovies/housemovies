<template>
  <q-img src="~assets/wall.jpg" class="window-width window-height">

    <q-page
      class="row justify-end items-center q-mr-lg"
    >
      <div class="column">
        <div class="row">
          <q-card square class="q-pa-md q-ma-none no-shadow" style="width:420px;">
            <q-card-section class="text-center">
              <q-img alt="flow logo" src="~assets/orbis.png" contain :ratio="16/9" style="height: 80px; width: 80%;"/>
            </q-card-section>
            <q-form class="q-gutter-md" ref="login"
                    @submit="onSubmit">
              <q-card-section>
                <l-input v-model="model.username" label="Usuario"
                         :rules="[
                $rules.required($t('validator.required'))
              ]"
                />
                <l-password v-model="model.password" label="Contraseña"
                            :rules="[
                $rules.required($t('validator.required'))
              ]"
                />
                <!--<q-input dark dense square filled clearable v-model="model.username" label="Email"
                         lazy-rules
                         :rules="[ val => !!val ||  'Este campo no puede estar en blanco.' ]">
                  <template v-slot:prepend>
                    <q-icon name="email"/>
                  </template>
                </q-input>
                <q-input dark dense square filled clearable v-model="model.password"
                         type="password" label="Password"
                         lazy-rules
                         :rules="[ val => !!val ||  'Este campo no puede estar en blanco.' ]">
                  <template v-slot:prepend>
                    <q-icon name="lock"/>
                  </template>
                </q-input>-->
                <p class="text-no-wrap text-grey text-caption text-right"> Olvido su Password ?</p>
                <q-btn type="submit" outline rounded size="md" color="red-4" class="full-width text-white" label="Ingresar"/>
              </q-card-section>
              <q-card-actions class="q-mt-none">
              </q-card-actions>
            </q-form>
          </q-card>
        </div>
      </div>
    </q-page>
  </q-img>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  data () {
    return {
      rulesModel: {},
      model: {
        username: '',
        password: ''
      }
    }
  },
  watch: {
    'model.username' (val) {
      console.log(val)
    }
  },
  methods: {
    ...mapActions('auth', ['login']),
    async onSubmit () {
      try {
        this.rulesModel = {}
        const validar = await this.$refs.login.validate()
        if (validar) {
          await this.login(this.model)
          await this.$router.replace({ name: 'home' })
        }
      } catch ({ status, message }) {
        if ([400].includes(status)) {
          this.rulesModel = message
        }
        console.log(status, message)
      }
    }
  }
}
</script>

<style scoped>

</style>
