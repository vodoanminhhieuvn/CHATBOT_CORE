from dataclasses import dataclass
from typing import List


@dataclass
class Meal:
    id: int
    imageType: str
    title: str
    readyInMinutes: int
    servings: int
    sourceUrl: str


@dataclass
class Nutrients:
    calories: float
    protein: float
    fat: float
    carbohydrates: float


@dataclass
class MealPlanResponse:
    meals: List[Meal]
    nutrients: Nutrients
