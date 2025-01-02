<template>
  <div>
    <v-container>
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold">Distillerie</h1>
        <v-btn @click="createDistillerie"> Créer une Distillerie </v-btn>
      </div>
      <v-data-table :headers="headers" :items="distilleries" :loading="loading">
        <template #item.actions="{ item }">
          <v-btn
            icon="mdi-eye"
            size="small"
            @click="openDistillerie(item.id)"
          />
          <v-btn
            icon="mdi-pencil"
            size="small"
            @click="editDistillerie(item.id)"
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
          <v-card-title class="headline">
            Confirmer la suppression
          </v-card-title>
          <v-card-text>
            Êtes-vous sûr de vouloir supprimer cette distillerie ?
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn color="blue darken-1" boolean @click="deleteDialog = false">
              Annuler
            </v-btn>
            <v-btn color="blue darken-1" boolean @click="deleteDistillerie">
              Confirmer
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useDistillerieStore } from '@/stores/distillerie'
import type { Distillery } from '@/types'

const distillerieStore = useDistillerieStore()
const deleteDialog = ref(false)
const distillerieToDelete = ref<Distillery | null>(null)
const { distilleries, loading } = storeToRefs(distillerieStore)
const router = useRouter()

const headers = [
  { title: 'Nom', key: 'name' },
  { title: 'Pays', key: 'country.data' },
  { title: 'Nb. de Whiskies', key: 'whiskies.length' },
  { title: 'Actions', key: 'actions' },
]

const confirmDelete = (distillerie: Distillery) => {
  distillerieToDelete.value = distillerie
  deleteDialog.value = true
}

const deleteDistillerie = async () => {
  if (distillerieToDelete.value?.id) {
    await distillerieStore.deleteDistillerie(distillerieToDelete.value.id)
    deleteDialog.value = false
    distillerieToDelete.value = null
  }
}

const openDistillerie = (id?: string) => {
  console.log(id)
  router.push({ name: '/Distillerie', query: { id } })
}

const createDistillerie = () => {
  router.push({ name: '/DistillerieEdit' })
}

const editDistillerie = (id?: string) => {
  router.push({ name: '/DistillerieEdit', query: { id } })
}

onMounted(async () => {
  await distillerieStore.fetchDistilleries()
})
</script>
