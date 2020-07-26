
const routes = [
  { path: '/principal/categoria/:id/:categoria', name: 'MenusAdministrar',  props: true, component: () => import('pages/menu/index.vue') },
  { path: '/principal/pelicula/:id', name: 'PeliculasDetalle',  props: true, component: () => import('pages/menu/pelicula.vue') },
  // { path: '/solicitud/solicitudes/crear/:id', name: 'SolicitudesCrearBasico', props: true, component: () => import('pages/solicitud/partial/crear.vue') },
  // { path: '/solicitud/solicitudes/crear', name: 'SolicitudesCrearBasico', component: () => import('pages/solicitud/partial/crear.vue') },
  // { path: '/solicitud/solicitudes/editar/:id', name: 'SolicitudesEditar', props: true, component: () => import('pages/inmueble/partial/editar.vue') }
]
export default routes
