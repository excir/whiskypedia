import { defineStore } from 'pinia'
import axios from 'axios'
import type { Negotiant } from '@/types'

const API_BASE = '/back'

interface NegociantState {
  negociants: Negotiant[]
  currentNegociant: Negotiant | null
  loading: boolean
  error: string | null
}

export const useNegociantStore = defineStore('negociant', {
  state: (): NegociantState => ({
    negociants: [],
    currentNegociant: null,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchNegociants(): Promise<void> {
      try {
        const response = await axios.get<Negotiant[]>(`${API_BASE}/negotiants`)
        this.negociants = response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
      }
    },

    async fetchNegociant(id: string): Promise<Negotiant | null> {
      try {
        const response = await axios.get<Negotiant>(
          `${API_BASE}/negotiants/${id}`
        )
        this.currentNegociant = response.data
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        return null
      }
    },

    async createNegociant(
      negociantData: Partial<Negotiant>
    ): Promise<Negotiant> {
      try {
        const response = await axios.post<Negotiant>(
          `${API_BASE}/negotiants`,
          negociantData
        )
        this.negociants.push(response.data)
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },

    async updateNegociant(
      id: string,
      negociantData: Partial<Negotiant>
    ): Promise<Negotiant> {
      try {
        const response = await axios.put<Negotiant>(
          `${API_BASE}/negotiants/${id}`,
          negociantData
        )
        const index = this.negociants.findIndex(
          (negociant) => negociant.id === id
        )
        if (index !== -1) {
          this.negociants[index] = response.data
        }
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },

    async deleteNegociant(id: string): Promise<void> {
      try {
        await axios.delete(`${API_BASE}/negotiants/${id}`)
        this.negociants = this.negociants.filter(
          (negociant) => negociant.id !== id
        )
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        throw error
      }
    },
  },
})
