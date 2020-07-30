<template>
  <div class="position-relative bg-grey-4" :style="style">
    <div class="WAL" style="height: 1%">
      <q-carousel
        animated
        v-model="slide"
        navigation
        infinite
        :autoplay="autoplay"
        arrows
        transition-prev="slide-right"
        transition-next="slide-left"
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
      >
        <q-carousel-slide :name="key"  v-for="(item, key) in imagenes" :key="key"  :img-src="item.imagen_carousel" />
      </q-carousel>
    </div>
    <q-layout view="lHh Lpr lFf" class="WAL__layout shadow-9" container>
      <q-header elevated>
        <q-toolbar class="bg-grey-3 text-black">
          <q-btn v-if="leftDrawerOpen == true" round flat icon="close" class="WAL__drawer-close" @click="leftDrawerOpen = !leftDrawerOpen"  />
          <q-btn v-if="leftDrawerOpen == false" round flat icon="menu" class="q-mr-sm" @click="leftDrawerOpen = !leftDrawerOpen" />

        </q-toolbar>
      </q-header>

      <q-drawer
        v-model="leftDrawerOpen"
        bordered
        :breakpoint="690"
        content-class="bg-grey-2"
      >
        <q-toolbar class="bg-grey-3">
          <q-avatar class="cursor-pointer">
            <img src="https://cdn.quasar.dev/app-icons/icon-128x128.png" />
          </q-avatar>
          <q-space />
        </q-toolbar>

        <!-- <q-toolbar class="bg-grey-2">
          <q-input rounded outlined dense class="WAL__field full-width" bg-color="white" v-model="search" placeholder="Buscar Pelicula">
            <template slot="prepend">
              <q-icon name="search" />
            </template>
          </q-input>
        </q-toolbar> -->

        <q-scroll-area style="height: calc(100% - 100px)">
          <menu-modulos @close="leftDrawerOpen = false"/>
          
        </q-scroll-area>
      </q-drawer>

      <q-page-container class="bg-grey-2">
        <router-view :key="$route.fullPath" />
      </q-page-container>

    </q-layout>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MainLayout',
  middleware: 'guest',
  data () {
    return {
      leftDrawerOpen: false,
      links: [],
      left: false,
      right: false,
      search: '',
      message: '',
      slide: 1,
      autoplay: true,
      imagenes: []
    }
  },
  computed: {
    ...mapGetters('menu', ['sub_menu_active']),
    style () {
      return {
        height: this.$q.screen.height + 'px'
      }
    }
  },
  mounted () {
    this.getMenus()
    this.getImagenesMuestra()
  },
  methods: {
    async getMenus () {
      try {
        const data = await this.Get('principal/menus')
        this.$store.commit('menu/modulos', data)
      } catch ({ message }) {
        console.error(message)
      }
    },
    async getImagenesMuestra () {
      try {
        this.imagenes = await this.Get('principal/pelicula/carousel')
      } catch ({ message }) {
        console.error(message)
      }
    }
  }
}
</script>

<style lang="sass">
.my-card
  width: 100%
  max-width: 165px
  height: 230px
  
.WAL
  width: 100%
  height: 1%
  padding-bottom: 20px
  &__layout
    margin: 0 auto
    z-index: 4000
    height: 95%
    width: 90%
    max-width: 1124px
    border-radius: 5px
  &__field.q-field--outlined .q-field__control:before
    border: none
  .q-drawer--standard
    .WAL__drawer-close
      display: none
@media (max-width: 850px)
  .WAL
    padding: 0
    &__layout
      width: 100%
      border-radius: 0
@media (min-width: 691px)
  .WAL
    &__drawer-open
      display: none
.conversation__summary
  margin-top: 4px
.conversation__more
  margin-top: 0!important
  font-size: 1.4rem
</style>
