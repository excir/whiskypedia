import { defineStore } from 'pinia'
import axios from 'axios'
import type { Negociant } from '@/types'

const API_BASE = '/back'

interface NegociantState {
  negociants: Negociant[]
  currentNegociant: Negociant | null
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
    async fetchNegociants(): Promise<Negociant[] | null> {
      try {
        const response = await axios.get<Negociant[]>(`${API_BASE}/negociants`)
        this.negociants = response.data
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        return null
      }
    },

    async fetchNegociant(id: string): Promise<Negociant | null> {
      try {
        const response = await axios.get<Negociant>(
          `${API_BASE}/negociants/${id}`
        )
        this.currentNegociant = response.data
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        return null
      }
    },

    async createNegociant(
      negociantData: Partial<Negociant>
    ): Promise<Negociant> {
      try {
        const response = await axios.post<Negociant>(
          `${API_BASE}/negociants`,
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
      negociantData: Partial<Negociant>
    ): Promise<Negociant> {
      negociantData.whiskies = undefined
      try {
        const response = await axios.put<Negociant>(
          `${API_BASE}/negociants/${id}`,
          negociantData
        )
        const index = this.negociants.findIndex(
          (negociant) => negociant.id === id
        )
        if (index !== undefined) {
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
        await axios.delete(`${API_BASE}/negociants/${id}`)
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
