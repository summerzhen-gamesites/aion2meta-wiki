export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.protocol !== "https:" || url.hostname === "www.aion2meta.wiki") {
      url.protocol = "https:";
      url.hostname = "aion2meta.wiki";
      return Response.redirect(url.toString(), 301);
    }

    const response = await env.ASSETS.fetch(request);
    if (url.pathname === "/dungeons/" || url.pathname === "/dungeons") {
      const headers = new Headers(response.headers);
      headers.set("Link", '<https://aion2meta.wiki/dungeons/>; rel="canonical"');
      return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers
      });
    }

    return response;
  }
};
