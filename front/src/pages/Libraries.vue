<template>
  <div class="p-4">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="6"
          v-for="libraryMap in libraryMaps"
          :key="libraryMap.name"
        >
          <LibraryList
            :name="libraryMap.name"
            @library-added="fetchLibraries"
            @library-deleted="fetchLibraries"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'
import { useLibraryStore } from '@/stores/library'
import LibraryList from '@/components/LibraryList.vue'

export default defineComponent({
  name: 'Libraries',
  components: {
    LibraryList,
  },
  setup() {
    const store = useLibraryStore()

    const fetchLibraries = async () => {
      await store.fetchLibraries()
    }

    onMounted(() => {
      fetchLibraries()
    })

    return {
      libraryMaps: store.libraryMap,
      fetchLibraries,
    }
  },
})
</script>

<style scoped>
.p-4 {
  padding: 1rem;
}
</style>
