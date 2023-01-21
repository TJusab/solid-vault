/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./solidvault/templates/**/*.html",
    "./solidvault/static/src/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
