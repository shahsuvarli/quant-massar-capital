export default async function fetchAPI(url: string, options?: RequestInit) {
    try {
        const res = await fetch(url, options)
        if (!res.ok) {
            throw new Error(res.statusText)
        }
        return res.json()
    }
    catch (err) {
        console.error(err)
        return []
    }
}