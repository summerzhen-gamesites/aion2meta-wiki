export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.protocol !== "https:" || url.hostname === "www.aion2meta.wiki") {
      url.protocol = "https:";
      url.hostname = "aion2meta.wiki";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  }
};
