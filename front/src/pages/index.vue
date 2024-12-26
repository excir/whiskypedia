<template>
  <div>
    <h1 class="text-2xl font-bold">Whisky</h1>
    <v-container>
      <v-data-table :headers="headers" :items="whiskies" :loading="loading">
        <template #item.actions="{ item }">
          <v-btn icon="mdi-eye" size="small" @click="openWhisky(item.id)" />
          <v-btn icon="mdi-pencil" size="small" @click="" />
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
import { ref, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useWhiskyStore } from '@/stores/whisky'
import type { Whisky } from '@/types'

const whiskyStore = useWhiskyStore()
const deleteDialog = ref(false)
const whiskyToDelete = ref<Whisky | null>(null)
const { whiskies, loading } = storeToRefs(whiskyStore)
const router = useRouter()

const headers = [
  { title: 'Nom', key: 'name' },
  { title: 'Distillerie', key: 'distillery.name' },
  { title: 'Type', key: 'whisky_type' },
  { title: '% Alcool', key: 'alcohol_percentage' },
  { title: 'Prix', key: 'price' },
  { title: 'Actions', key: 'actions' },
]

// const confirmDelete = (whisky: Whisky) => {
//   whiskyToDelete.value = whisky
//   deleteDialog.value = true
// }

const openWhisky = (id: string) => {
  console.log(id)
  router.push({ name: '/Whisky', query: { id } })
}

onMounted(async () => {
  await whiskyStore.fetchWhiskies()
})
</script>
