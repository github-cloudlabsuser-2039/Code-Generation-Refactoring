const fetch = require('node-fetch');

const API_KEY = "1b2779136b135a448d57340fd5fd3067";
const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

/**
 * Fetches weather data for a given city from OpenWeatherMap API.
 * @param {string} city - The name of the city to fetch weather for.
 * @returns {Promise<object>} - The weather data for the city.
 */
async function getWeatherByCity(city) {
    try {
        const response = await fetch(`${BASE_URL}?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric`);
        if (!response.ok) {
            throw new Error(`Error fetching weather data: ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

// Example usage:
getWeatherByCity("London")
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));