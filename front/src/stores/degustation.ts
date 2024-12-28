import { defineStore } from 'pinia'
import axios from 'axios'
import type { Tasting } from '@/types'

// src/stores/degustation.ts

const API_BASE = '/back'

interface TastingState {
  tastings: Tasting[]
  loading: boolean
  error: string | null
}

export const useTastingStore = defineStore('tasting', {
  state: (): TastingState => ({
    tastings: [],
    loading: false,
    error: null,
  }),

  actions: {
    async addTasting(tastingData: Partial<Tasting>): Promise<Tasting> {
      try {
        const response = await axios.post<Tasting>(
          `${API_BASE}/tastings`,
          tastingData
        )
        this.tastings.push(response.data)
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },

    async deleteTasting(id: string): Promise<void> {
      try {
        await axios.delete(`${API_BASE}/tastings/${id}`)
        this.tastings = this.tastings.filter((tasting) => tasting.id !== id)
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },
  },
})
