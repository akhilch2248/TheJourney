# 🗄️ Data Model – The Journey App

## Tables

### Users
- `id` (UUID, PK)
- `auth_provider` (Apple, Google, Email)
- `email`
- `created_at`

### Weights
- `id` (UUID, PK)
- `user_id` (FK Users)
- `date`
- `weight_kg`

### Foods
- `id` (UUID, PK)
- `user_id` (FK Users)
- `name`
- `protein`
- `carbs`
- `fat`
- `calories`
- `custom_flag` (boolean)

### Meals
- `id` (UUID, PK)
- `user_id` (FK Users)
- `date`
- `food_id` (FK Foods)
- `quantity_g`

### Workouts
- `id` (UUID, PK)
- `user_id` (FK Users)
- `date`
- `type` (swim, gym, walk, etc.)
- `duration_min`
- `calories_burned`
- `source` (HealthKit/manual)

### DeficitLog
- `id` (UUID, PK)
- `user_id` (FK Users)
- `date`
- `calories_in`
- `calories_out`
- `deficit`
- `streak_flag`
