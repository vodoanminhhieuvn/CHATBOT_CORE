from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict


class Title(Enum):
    Nextpage = "Next page"
    Self = "Self"


@dataclass
class Next:
    href: str
    title: Title


@dataclass
class HitLinks:
    linksself: Next


class Caution(Enum):
    FODMAP = "FODMAP"
    Soy = "Soy"
    Sulfites = "Sulfites"


class DietLabel(Enum):
    Balanced = "Balanced"
    HighFiber = "High-Fiber"
    LowCarb = "Low-Carb"


class SchemaOrgTag(Enum):
    carbohydrateContent = "carbohydrateContent"
    cholesterolContent = "cholesterolContent"
    fatContent = "fatContent"
    fiberContent = "fiberContent"
    proteinContent = "proteinContent"
    saturatedFatContent = "saturatedFatContent"
    sodiumContent = "sodiumContent"
    sugarContent = "sugarContent"
    transFatContent = "transFatContent"


class Unit(Enum):
    empty = "%"
    g = "g"
    kcal = "kcal"
    mg = "mg"
    µg = "µg"


@dataclass
class Digest:
    label: str
    tag: str
    total: float
    hasRDI: bool
    daily: float
    unit: Unit
    schemaOrgTag: Optional[SchemaOrgTag] = None
    sub: Optional[List['Digest']] = None


@dataclass
class Regular:
    url: str
    width: int
    height: int


@dataclass
class Images:
    THUMBNAIL: Regular
    SMALL: Regular
    REGULAR: Regular
    LARGE: Optional[Regular] = None


@dataclass
class Ingredient:
    text: str
    quantity: float
    food: str
    weight: float
    foodId: str
    measure: Optional[str] = None
    foodCategory: Optional[str] = None
    image: Optional[str] = None


class MealType(Enum):
    brunch = "brunch"
    lunchdinner = "lunch/dinner"


@dataclass
class Total:
    label: str
    quantity: float
    unit: Unit


@dataclass
class Recipe:
    uri: str
    label: str
    image: str
    images: Images
    source: str
    url: str
    shareAs: str
    recipeyield: int
    dietLabels: List[DietLabel]
    healthLabels: List[str]
    cautions: List[Caution]
    ingredientLines: List[str]
    ingredients: List[Ingredient]
    calories: float
    totalWeight: float
    totalTime: int
    cuisineType: List[str]
    mealType: List[MealType]
    dishType: List[str]
    totalNutrients: Dict[str, Total]
    totalDaily: Dict[str, Total]
    digest: List[Digest]


@dataclass
class Hit:
    recipe: Recipe
    links: HitLinks


@dataclass
class RecipeResponseLinks:
    next: Next


@dataclass
class RecipeResponse:
    RecipeResponsefrom: int
    to: int
    count: int
    links: RecipeResponseLinks
    hits: List[Hit]
