// src/types/index.ts
export interface Whisky {
  id?: string
  name: string
  distillery_id: string | null
  negociant_id?: string | null
  alcohol_percentage: number
  whisky_type_id: string
  bottle_size_cl: number
  price: number
  is_peated: boolean
  nose?: string
  appearance?: string
  palate?: string
  finish?: string
  photo?: string
  distillery?: Distillery
  negociant?: Negociant
  whisky_type?: Library
  tastings?: Tasting[]
}

export interface Distillery {
  id?: string
  name: string
  country_id: string
  notes?: string
  whiskies?: Whisky[]
  country?: Library
}

export interface Negociant {
  id?: string
  name: string
  country_id?: string
  notes?: string
  whiskies?: Whisky[]
  country?: Library
}

export interface Tasting {
  id?: string
  whisky_id: string
  rating: number
  tasting_date: Date
}

export interface Library {
  id?: string
  name: string
  data: string
}
