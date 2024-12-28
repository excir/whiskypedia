<template>
  <div>
    <h1 class="text-2xl font-bold">Whisky</h1>
    <v-btn @click="createWhisky">Créer un Whisky</v-btn>
    <v-container>
      <v-data-table
        :headers="headers"
        :items="whiskiesWithRatings"
        :loading="loading"
      >
        <template #item.averageRating="{ item }">
          <v-rating
            half-increments
            :length="5"
            :size="28"
            color="warning"
            active-color="warning"
            :model-value="item.averageRating"
            readonly
          />
        </template>
        <template #item.actions="{ item }">
          <v-btn icon="mdi-eye" size="small" @click="openWhisky(item.id)" />
          <v-btn icon="mdi-pencil" size="small" @click="editWhisky(item.id)" />
          <v-btn icon="mdi-delete" size="small" color="error" @click="" />
        </template>
      </v-data-table>

      <v-dialog v-model="deleteDialog" max-width="400">
        <!-- Dialog content -->
      </v-dialog>
    </v-container>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { useWhiskyStore } from '@/stores/whisky'
import type { Whisky } from '@/types'

const whiskyStore = useWhiskyStore()
const deleteDialog = ref(false)
const whiskyToDelete = ref<Whisky | null>(null)
const { whiskies, loading } = storeToRefs(whiskyStore)
const router = useRouter()

const whiskiesWithRatings = computed(() => {
  return whiskies.value.map((whisky) => {
    if (!whisky.tastings || whisky.tastings.length === 0) {
      return { ...whisky, averageRating: undefined }
    }
    const total = whisky.tastings.reduce(
      (sum, tasting) => sum + tasting.rating,
      0
    )
    const averageRating = total / whisky.tastings.length / 2
    return { ...whisky, averageRating }
  })
})

const headers = [
  { title: 'Nom', key: 'name' },
  { title: 'Distillerie', key: 'distillery.name' },
  { title: 'Pays', key: 'distillery.country' },
  { title: 'Type', key: 'whisky_type' },
  { title: 'Note Moyenne', key: 'averageRating' },
  { title: 'Actions', key: 'actions' },
]

// const confirmDelete = (whisky: Whisky) => {
//   whiskyToDelete.value = whisky
//   deleteDialog.value = true
// }

const createWhisky = () => {
  router.push({ name: '/WhiskyEdit' })
}

const editWhisky = (id?: string) => {
  if (id) router.push({ name: '/WhiskyEdit', query: { id } })
}

const openWhisky = (id?: string) => {
  if (id) router.push({ name: '/Whisky', query: { id } })
}

onMounted(async () => {
  await whiskyStore.fetchWhiskies()
})
</script>
