<template>
  <div>
    <v-container>
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold">Négociant</h1>
        <v-btn @click="createNegociant">Créer un Négociant</v-btn>
      </div>
      <v-data-table :headers="headers" :items="negociants" :loading="loading">
        <template #item.actions="{ item }">
          <v-btn icon="mdi-eye" size="small" @click="openNegociant(item.id)" />
          <v-btn
            icon="mdi-pencil"
            size="small"
            @click="editNegociant(item.id)"
          />
          <v-btn
            icon="mdi-delete"
            size="small"
            color="error"
            @click="confirmDelete(item)"
          />
        </template>
      </v-data-table>

      <v-dialog v-model="deleteDialog" max-width="400">
        <v-card>
          <v-card-title class="headline">Confirmer la suppression</v-card-title>
          <v-card-text
            >Êtes-vous sûr de vouloir supprimer ce négociant ?</v-card-text
          >
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" boolean @click="deleteDialog = false"
              >Annuler</v-btn
            >
            <v-btn color="blue darken-1" boolean @click="deleteNegociant"
              >Confirmer</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useNegociantStore } from '@/stores/negociant'
import type { Negociant } from '@/types'

const negociantStore = useNegociantStore()
const deleteDialog = ref(false)
const negociantToDelete = ref<Negociant | null>(null)
const { negociants, loading } = storeToRefs(negociantStore)
const router = useRouter()

const headers = [
  { title: 'Nom', key: 'name' },
  { title: 'Pays', key: 'country.data' },
  { title: 'Nb. de Whiskies', key: 'whiskies.length' },
  { title: 'Actions', key: 'actions' },
]

const confirmDelete = (negociant: Negociant) => {
  negociantToDelete.value = negociant
  deleteDialog.value = true
}

const deleteNegociant = async () => {
  if (negociantToDelete.value?.id) {
    await negociantStore.deleteNegociant(negociantToDelete.value.id)
    deleteDialog.value = false
    negociantToDelete.value = null
  }
}

const createNegociant = () => {
  router.push({ name: '/NegociantEdit' })
}

const editNegociant = (id?: string) => {
  router.push({ name: '/NegociantEdit', query: { id } })
}

const openNegociant = (id?: string) => {
  console.log(id)
  router.push({ name: '/Negociant', query: { id } })
}

onMounted(async () => {
  await negociantStore.fetchNegociants()
})
</script>
