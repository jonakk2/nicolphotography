<script>
  import { Router, Link, Route } from "svelte-routing";

  // Moody theme
  import Home from "./themes/moody/Home.svelte";

  // Other pages
  import About from "./lib/About.svelte";
  import Akce from "./lib/Akce.svelte";
  import VanocniFoceni from "./lib/VanocniFoceni.svelte";
  import Cenik from "./lib/Cenik.svelte";
  import Kontakt from "./lib/Kontakt.svelte";
  import PrivacyPolicy from "./lib/PrivacyPolicy.svelte";
  import ObchodniPodminky from "./lib/ObchodniPodminky.svelte";
  import Pruvodce from "./lib/Pruvodce.svelte";
  import CookieConsent from "./lib/CookieConsent.svelte";
  import MobileQuickContact from "./lib/MobileQuickContact.svelte";
  import ScrollToTop from "./lib/ScrollToTop.svelte";
  import NotFound from "./lib/NotFound.svelte";
</script>

<Router>
  <div>
    <Route path="/" component={Home} />
    <Route path="/about" component={About} />
    <Route path="/portfolio" component={Akce} />
    <Route path="/akce" component={VanocniFoceni} />
    <Route path="/vanocni-foceni" component={VanocniFoceni} />
    <Route path="/cenik" component={Cenik}/>
    <Route path="/pruvodce" component={Pruvodce}/>
    <Route path="/kontakt" component={Kontakt}/>
    <Route path="/ochrana-udaju" component={PrivacyPolicy}/>
    <Route path="/obchodni-podminky" component={ObchodniPodminky}/>
    <Route path="*" component={NotFound} />
  </div>
</Router>

<ScrollToTop />
<MobileQuickContact />
<CookieConsent />
