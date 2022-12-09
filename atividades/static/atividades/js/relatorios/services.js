export async function getAtividadesAno(ano) {
    const atividades = await fetch(`/api/atividades/ano/${ano}/`);
    let data = await atividades.json()
    data.sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
    return data;
}