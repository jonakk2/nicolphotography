<script>
  import { Router, Link, Route } from "svelte-routing";

  // Moody theme
  import Home from "./themes/moody/Home.svelte";

  // Other pages
  import About from "./lib/About.svelte";
  import Akce from "./lib/Akce.svelte";
  import Cenik from "./lib/Cenik.svelte";
  import Kontakt from "./lib/Kontakt.svelte";
  import PrivacyPolicy from "./lib/PrivacyPolicy.svelte";
</script>

<Router>
  <div>
    <Route path="/" component={Home} />
    <Route path="/about" component={About} />
    <Route path="/akce" component={Akce} />
    <Route path="/cenik" component={Cenik}/>
    <Route path="/kontakt" component={Kontakt}/>
    <Route path="/ochrana-udaju" component={PrivacyPolicy}/>
  </div>
</Router>
