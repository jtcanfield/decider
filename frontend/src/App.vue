<template>
  <div id="app">
    <section class="i-am-useless">
      <div class="mdc-card demo-card">
        <div class="mdc-card__primary-action demo-card__primary-action" tabindex="0">
          <div class="demo-card__primary" @click="addClass = !addClass">
            <h2
              class="demo-card__title mdc-typography mdc-typography--headline6"
            >Check this out</h2>
            <img alt="Vue logo" src="./assets/logo.png" :class="addClass ? 'big' : 'not-big'" />
          </div>
        </div>
        <div class="mdc-card__actions">
          <div class="mdc-card__action-buttons">
            <button
              @click="addClass = !addClass"
              class="mdc-button mdc-card__action mdc-card__action--button"
            >Click Me</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      addClass: false
    };
  }
};
</script>

<style>
html {
  background-color: grey;
}
.not-big {
  transition: all 1s ease-in-out;
  margin: 0 auto;
  width: 100px;
  height: 100px;
}
.big {
  transition: all 1s ease-in-out;
  margin: 0 auto;
  width: 400px;
  height: 400px;
}
.mdc-card__actions {
  justify-content: center;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
