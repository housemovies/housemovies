<template>
<div :class="`col-${col} ${class_val}`" v-if="value.deudores.length > 0" >
  <q-field class="col-12" filled  label="Listado de Deudores Solidarios" stack-label>
    <template v-slot:control>
      <div class="col-12">
        <q-markup-table class="my-sticky-header-column-table" >
          <thead>
            <tr>
              <th class="bg-primary text-white" > Documento </th>
              <th class="bg-primary text-white" > Nombre Deudor Solidario</th>
            </tr>
          </thead>
          <tbody>
            <tr  v-for="col in value.deudores" :key="col.documento">
              <td > {{ col.documento }} </td>
              <td > {{ col.n_completo }} </td>
            </tr>
          </tbody>
        </q-markup-table>
      </div>
    </template>
  </q-field>
</div>
</template>

<script>
export default {
  name: 'ListadoDeudores',
  props: {
    col: {
      type: String,
      default: '12'
    },
    class_val: {
      type: String,
      default: ''
    },
    buscador: {
      type: Boolean,
      default: false
    },
    value: {
      type: Object
    }
  },
  data () {
    return {
      columns: [
        {
          name: 'documento',
          required: true,
          label: 'Documento',
          align: 'left',
          field: row => row.documento,
          sortable: true,
          classes: 'bg-grey-2 ellipsis',
          style: 'min-width: 50px',
          headerClasses: 'bg-primary text-white'
        },
        {
          name: 'n_completo',
          required: true,
          label: 'Nombre Deudor',
          align: 'left',
          field: row => row.n_completo,
          sortable: true
        }
      ]
    }
  }
  // watch: {
  //   'value' (val) {
  //     if (val !== '' && val !== null) {
  //       this.editar_direccion(val)
  //     }
  //   }
  // },
  // computed: {
  //   direccionC () {
  //     console.log('aca tambien ', this.value)
  //     let temp = ''
  //     if (this.value == '') {
  //     } else {
  //       this.editar_direccion(this.value)
  //     }
  //     return temp
  //   }
  // },
  // mounted () {
  //   this.getRecursos()
  // }
  // methods: {
  // }
}
</script>

<style lang="sass">
.my-sticky-header-column-table
  /* height or max-height is important */
  height: 100%

  /* specifying max-width so the example can
    highlight the sticky column on any browser window */
  max-width: 100%

  td:first-child
    /* bg color is important for td; just specify one */
    background-color: #f5f5f5 !important

  tr th
    position: sticky
    /* higher than z-index for td below */
    z-index: 2
    /* bg color is important; just specify one */
    background: #f5f5f5

  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
    /* highest z-index */
    z-index: 3
  thead tr:first-child th
    top: 0
    z-index: 1
  tr:first-child th:first-child
    /* highest z-index */
    z-index: 3

  td:first-child
    z-index: 1

  td:first-child, th:first-child
    position: sticky
    left: 0
</style>
