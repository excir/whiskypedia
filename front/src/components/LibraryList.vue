<template>
  <div class="p-4">
    <v-card>
      <v-card-text>
        <v-data-table :headers="headers" :items="libraries" class="elevation-1">
          <template #top>
            <v-toolbar flat>
              <v-toolbar-title>{{ name }}</v-toolbar-title>
              <v-divider class="mx-4" inset vertical />
              <v-spacer />
              <v-btn color="primary" @click="showAddDialog = true">
                Add {{ name }}
              </v-btn>
            </v-toolbar>
          </template>
          <template #item.actions="{ item }">
            <v-btn icon @click="editLibrary(item)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn icon color="error" @click="confirmDeleteLibrary(item.id)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>

    <v-dialog v-model="showAddDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Add {{ name }}</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-text-field v-model="newLibrary.data" label="Data" required />
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="blue darken-1" text @click="showAddDialog = false">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="addLibrary"> Add </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="showEditDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Edit {{ name }}</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="editForm">
            <v-text-field
              v-model="editLibraryData.data"
              label="Data"
              required
            />
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="blue darken-1" text @click="showEditDialog = false">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="updateLibrary">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Dialog de confirmation de suppression -->
    <v-dialog v-model="showDeleteDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Confirmer la suppression</span>
        </v-card-title>
        <v-card-text>
          Êtes-vous sûr de vouloir supprimer cet élément ?
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="blue darken-1" text @click="showDeleteDialog = false">
            Annuler
          </v-btn>
          <v-btn color="blue darken-1" text @click="deleteLibrary">
            Supprimer
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue'
import { useLibraryStore } from '@/stores/library'

import type { Library } from '@/types'

export default defineComponent({
  name: 'LibraryList',
  props: {
    name: {
      type: String,
      required: true,
    },
  },
  setup(props, { emit }) {
    const store = useLibraryStore()
    const showAddDialog = ref(false)
    const newLibrary = ref<Library>({ name: props.name, data: '' })
    const showEditDialog = ref(false)
    const editLibraryData = ref<Library>({ name: props.name, data: '' })
    const showDeleteDialog = ref(false)
    const libraryToDelete = ref<string | null>(null)

    const headers = [
      { text: 'Data', value: 'data' },
      { text: 'Actions', value: 'actions', sortable: false },
    ]

    const libraries = computed(() => {
      const libraryMap = store.libraryMap.find(
        (libMap) => libMap.name === props.name
      )
      return libraryMap
        ? libraryMap.libraries.sort((a, b) => a.data.localeCompare(b.data))
        : []
    })

    const addLibrary = async () => {
      await store.addLibrary(newLibrary.value)
      showAddDialog.value = false
      newLibrary.value = { name: props.name, data: '' }
      emit('library-added', newLibrary.value)
    }

    const confirmDeleteLibrary = (libraryId: string) => {
      libraryToDelete.value = libraryId
      showDeleteDialog.value = true
    }

    const deleteLibrary = async () => {
      if (libraryToDelete.value) {
        await store.deleteLibrary(libraryToDelete.value)
        emit('library-deleted', libraryToDelete.value)
        libraryToDelete.value = null
      }
      showDeleteDialog.value = false
    }

    const editLibrary = (library: Library) => {
      editLibraryData.value = { ...library }
      showEditDialog.value = true
    }

    const updateLibrary = async () => {
      await store.updateLibrary(editLibraryData.value)
      showEditDialog.value = false
      emit('library-updated', editLibraryData.value)
    }

    return {
      headers,
      libraries,
      showAddDialog,
      newLibrary,
      addLibrary,
      deleteLibrary,
      showEditDialog,
      editLibraryData,
      editLibrary,
      updateLibrary,
      showDeleteDialog,
      confirmDeleteLibrary,
      libraryToDelete,
    }
  },
})
</script>

<style scoped>
.p-4 {
  padding: 1rem;
}
</style>
