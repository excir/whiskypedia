<template>
  <div>
    <Negociant v-if="negociant" :negociant="negociant" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useNegociantStore } from '@/stores/negociant'
import Negociant from '@/components/Negociant.vue'

export default {
  name: 'NegociantPage',
  components: {
    Negociant,
  },
  setup() {
    const route = useRoute()
    const negociantStore = useNegociantStore()
    const negociant = ref(null)

    onMounted(async () => {
      negociant.value = await negociantStore.fetchNegociant(route.query.id)
    })

    return {
      negociant,
    }
  },
}
</script>

<style scoped>
/* Add your styles here */
</style>
