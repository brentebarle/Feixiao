import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('WOLFRAM_ALPHA_APP_ID')
TOKEN = os.getenv('DISCORD_TOKEN')
PRIORITY_LIST = ["3d plots", "3d plot", "2d plots", "2d plot", "image"]

sample_queries = [
    "Solve x^2 - 4x + 4 = 0",
    "Derivative of sin(x) * e^x",
    "Integrate x^3 * e^x dx",
    "Boiling point of water at sea level",
    "Distance from Earth to the Sun in kilometers",
    "Chemical formula of caffeine",
    "President of France",
    "Capital of Australia",
    "Current population of Tokyo",
    "Convert 100 USD to EUR",
    "Stock price of Apple Inc.",
    "Compound interest on 5000 USD at 5% annual rate for 10 years",
    "Current temperature in New York City",
    "Weather forecast for Paris next week",
    "Highest mountain in the world",
    "Coordinates of the Eiffel Tower",
    "Calories in a medium-sized apple",
    "Nutritional facts of 100 grams of spinach",
    "Convert 5 miles to kilometers",
    "Convert 100 grams to ounces",
    "Current phase of the Moon",
    "Next visible transit of Venus from Earth",
    "Nobel Prize in Literature winner 2023",
    "Most spoken languages in the world",
    "Solve x^2 + y^2 = 25 and x - y = 1",
    "Fourier transform of sin(x) * e^(-x^2)",
    "Eigenvalues of matrix [[1, 2], [3, 4]]",
    "Laplace transform of t^2 * e^(-3t)",
    "Gibbs free energy of reaction with ΔH = -40 kJ/mol and ΔS = 100 J/(mol*K) at 298 K",
    "Solve dy/dx = x^2 * y",
    "Roots of polynomial x^4 - 3x^3 + 2x^2 - 5x + 6",
    "Integral of 1/(x^2 + 1) from 0 to infinity",
    "Time complexity of merge sort",
    "Eigenvectors of matrix [[2, -1], [-1, 2]]",
    "Steady-state solution of d^2y/dx^2 + 4dy/dx + 4y = 0",
    "pH of 0.01 M hydrochloric acid solution",
    "Area of triangle with vertices (1,2), (3,4), and (5,6)",
    "Entropy change when 100 g of ice melts at 0°C",
    "Volume of solid of revolution of y = x^2 around x-axis from x = 0 to x = 2",
    "Convergence of series ∑ (1/n^2) from n=1 to infinity",
    "Determinant of matrix [[2, 3, 1], [4, 5, 2], [7, 8, 3]]",
    "Solution to x^3 - 2x + 1 = 0 using numerical methods",
    "Probability density function of normal distribution with mean 0 and standard deviation 1",
    "Value of Riemann zeta function at s = 2",
    "Fourier series of f(x) = x^2 on [-π, π]",
    "Limit of (sin(x)/x) as x approaches 0",
]
