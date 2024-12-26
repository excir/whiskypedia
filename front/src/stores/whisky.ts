// src/stores/whisky.ts
import { defineStore } from 'pinia'
import axios from 'axios'
import type { Whisky } from '@/types'

const API_BASE = '/back'

interface WhiskyState {
  whiskies: Whisky[]
  currentWhisky: Whisky | null
  loading: boolean
  error: string | null
}

export const useWhiskyStore = defineStore('whisky', {
  state: (): WhiskyState => ({
    whiskies: [],
    currentWhisky: null,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchWhiskies(): Promise<void> {
      try {
        const response = await axios.get<Whisky[]>(`${API_BASE}/whiskies`)
        this.whiskies = response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
      }
    },

    async fetchWhisky(id: string): Promise<Whisky | null> {
      try {
        const response = await axios.get<Whisky>(`${API_BASE}/whiskies/${id}`)
        this.currentWhisky = response.data
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        return null
      }
    },

    async createWhisky(whiskyData: Partial<Whisky>): Promise<Whisky> {
      try {
        const response = await axios.post<Whisky>(
          `${API_BASE}/whiskies`,
          whiskyData
        )
        this.whiskies.push(response.data)
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },

    async fetchWhiskyDetailsById(id: string): Promise<Whisky | null> {
      try {
        const response = await axios.get<Whisky>(
          `${API_BASE}/whiskies/${id}/details`
        )
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        return null
      }
    },

    async updateWhisky(
      id: string,
      whiskyData: Partial<Whisky>
    ): Promise<Whisky> {
      try {
        const response = await axios.put<Whisky>(
          `${API_BASE}/whiskies/${id}`,
          whiskyData
        )
        const index = this.whiskies.findIndex((whisky) => whisky.id === id)
        if (index !== -1) {
          this.whiskies[index] = response.data
        }
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },

    async deleteWhisky(id: string): Promise<void> {
      try {
        await axios.delete(`${API_BASE}/whiskies/${id}`)
        this.whiskies = this.whiskies.filter((whisky) => whisky.id !== id)
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },
    // Autres actions avec types...
  },
})
