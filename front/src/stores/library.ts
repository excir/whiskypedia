import { defineStore } from 'pinia'
import axios from 'axios'
import type { Library } from '@/types'
import { useNotification } from '@/services/notification-services'

const API_BASE = '/back'
const { addNotification } = useNotification()

const libraryNames = ['whisky_types', 'countries']

export interface LibraryMap {
  name: string
  libraries: Library[]
}

export const useLibraryStore = defineStore('library', {
  state: () => ({
    libraryMap: [] as LibraryMap[],
  }),
  actions: {
    async fetchLibraries() {
      try {
        const response = await axios.get(`${API_BASE}/library`)
        const libraries: Library[] = Array.isArray(response.data)
          ? response.data
          : []
        console.log('libraries:', libraries)

        const map = libraries.reduce((acc: LibraryMap[], library: Library) => {
          const libraryMap = acc.find((libMap) => libMap.name === library.name)
          if (libraryMap) {
            libraryMap.libraries.push(library)
          } else {
            acc.push({ name: library.name, libraries: [library] })
          }
          return acc
        }, [])

        // Ensure libraryMap contains entries for each name in libraryNames
        libraryNames.forEach((name) => {
          if (!map.find((libMap) => libMap.name === name)) {
            map.push({ name, libraries: [] })
          }
        })

        this.libraryMap.splice(0, this.libraryMap.length, ...map)
      } catch (error) {
        console.error('Error fetching libraries:', error)
        addNotification('Erreur !', 'error')
      }
    },
    async addLibrary(library: Library) {
      try {
        const response = await axios.post(`${API_BASE}/library`, library)
        this.merge(library, 'add')
        addNotification('Item ajouté', 'success')
      } catch (error) {
        console.error('Error adding library:', error)
        addNotification('Erreur !', 'error')
      }
    },
    async deleteLibrary(libraryId: string) {
      try {
        await axios.delete(`${API_BASE}/library/${libraryId}`)
        this.merge({ id: libraryId } as Library, 'delete')
        addNotification('Item supprimé', 'success')
      } catch (error) {
        console.error('Error deleting library:', error)
        addNotification('Erreur !', 'error')
      }
    },
    async updateLibrary(library: Library) {
      try {
        const response = await axios.put(
          `${API_BASE}/library/${library.id}`,
          library
        )
        this.merge(library, 'update')
        addNotification('Item mis à jour', 'success')
      } catch (error) {
        console.error('Error updating library:', error)
        addNotification('Erreur !', 'error')
      }
    },
    async fetchLibrary(name: string): Promise<Library[]> {
      if (this.libraryMap.length === 0) {
        await this.fetchLibraries()
      }
      const libraryMap = this.libraryMap.find((libMap) => libMap.name === name)
      return libraryMap ? libraryMap.libraries : []
    },
    merge(library: Library, action: 'add' | 'delete' | 'update') {
      const libraryMap = this.libraryMap.find(
        (libMap) => libMap.name === library.name
      )
      if (action === 'add') {
        if (libraryMap) {
          libraryMap.libraries.push(library)
        } else {
          this.libraryMap.push({ name: library.name, libraries: [library] })
        }
      } else if (action === 'delete') {
        if (libraryMap) {
          libraryMap.libraries = libraryMap.libraries.filter(
            (lib) => lib.id !== library.id
          )
          if (libraryMap.libraries.length === 0) {
            this.libraryMap = this.libraryMap.filter(
              (libMap) => libMap.name !== library.name
            )
          }
        }
      } else if (action === 'update') {
        if (libraryMap) {
          const index = libraryMap.libraries.findIndex(
            (lib) => lib.id === library.id
          )
          if (index !== -1) {
            libraryMap.libraries[index] = library
          }
        }
      }
    },
  },
})
