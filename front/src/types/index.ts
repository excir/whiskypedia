// src/types/index.ts
export interface Whisky {
  id: string
  name: string
  distillery_id: string
  negotiant_id?: string
  alcohol_percentage: number
  whisky_type: string
  bottle_size_cl: number
  price: number
  is_peated: boolean
  nose?: string
  appearance?: string
  palate?: string
  finish?: string
  photo?: string
  distillery?: Distillery
  negotiant?: Negotiant
  tastings?: Tasting[]
}

export interface Distillery {
  id: string
  name: string
  country: string
  notes?: string
  whiskies?: Whisky[]
}

export interface Negotiant {
  id: string
  name: string
  country?: string
  notes?: string
  whiskies?: Whisky[]
}

export interface Tasting {
  id: string
  whisky_id: string
  rating: number
  tasting_date: string
  whisky?: Whisky
}
