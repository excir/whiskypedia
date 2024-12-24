// src/stores/whisky.ts
import { defineStore } from 'pinia'
import axios from 'axios'
import type { Whisky } from '@/types'

const API_BASE = '/back'

interface WhiskyState {
  whiskies: Whisky[];
  currentWhisky: Whisky | null;
  loading: boolean;
  error: string | null;
}

export const useWhiskyStore = defineStore('whisky', {
  state: (): WhiskyState => ({
    whiskies: [],
    currentWhisky: null,
    loading: false,
    error: null
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
    
    async createWhisky(whiskyData: Partial<Whisky>): Promise<Whisky> {
      try {
        const response = await axios.post<Whisky>(`${API_BASE}/whiskies`, whiskyData)
        this.whiskies.push(response.data)
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    }
    // Autres actions avec types...
  }
})