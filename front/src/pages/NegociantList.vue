<template>
  <div>
    <h1 class="text-2xl font-bold">Négociant</h1>
    <v-container>
      <v-data-table :headers="headers" :items="negociants" :loading="loading">
        <template #item.actions="{ item }">
          <v-btn icon="mdi-eye" size="small" @click="openNegociant(item.id)" />
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
import { useNegociantStore } from '@/stores/negociant'
import type { Negotiant } from '@/types'

const negociantStore = useNegociantStore()
const deleteDialog = ref(false)
const negociantToDelete = ref<Negotiant | null>(null)
const { negociants, loading } = storeToRefs(negociantStore)
const router = useRouter()

const headers = [
  { title: 'Nom', key: 'name' },
  { title: 'Pays', key: 'country' },
  { title: 'Actions', key: 'actions' },
]

// const confirmDelete = (negociant: Negotiant) => {
//   negociantToDelete.value = negociant
//   deleteDialog.value = true
// }

const openNegociant = (id: string) => {
  console.log(id)
  router.push({ name: '/Negociant', query: { id } })
}

onMounted(async () => {
  await negociantStore.fetchNegociants()
})
</script>
