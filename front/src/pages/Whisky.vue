<template>
  <div>
    <Whisky v-if="whisky" :whisky="whisky" />
  </div>
  <div>
    <NotationList
      v-if="whisky"
      :whiskyId="whisky.id"
      :initialTastings="whisky.tastings"
      @update-whisky="updateWhisky"
    />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useWhiskyStore } from '@/stores/whisky'
import Whisky from '@/components/Whisky.vue'
import NotationList from '@/components/NotationList.vue' // Ajout de l'import

export default {
  name: 'WhiskyPage',
  components: {
    Whisky,
    NotationList, // Ajout du composant
  },
  setup() {
    const route = useRoute()
    const whiskyStore = useWhiskyStore()
    const whisky = ref(null)

    onMounted(async () => {
      whisky.value = await whiskyStore.fetchWhiskyDetailsById(route.query.id)
    })

    const updateWhisky = async () => {
      whisky.value = await whiskyStore.fetchWhiskyDetailsById(route.query.id)
    }

    return {
      whisky,
      updateWhisky,
    }
  },
}
</script>

<style scoped>
/* Add your styles here */
</style>
