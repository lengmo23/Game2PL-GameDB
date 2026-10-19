import { readdir, readFile, writeFile, mkdir } from "node:fs/promises";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const recordsRoot = join(root, "records");

async function jsonFiles(directory) {
  const result = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) result.push(...await jsonFiles(path));
    else if (entry.isFile() && entry.name.endsWith(".json")) result.push(path);
  }
  return result;
}

const records = [];
const ids = new Set();
for (const path of await jsonFiles(recordsRoot)) {
  const record = JSON.parse(await readFile(path, "utf8"));
  if (record.schemaVersion !== 1 || typeof record.id !== "string" || typeof record.status !== "string")
    throw new Error(`Invalid record: ${relative(root, path)}`);
  if (ids.has(record.id)) throw new Error(`Duplicate id: ${record.id}`);
  if (record.id !== `${record.platform}:${record.platformId}`)
    throw new Error(`ID mismatch: ${relative(root, path)}`);
  ids.add(record.id);
  records.push(record);
}
records.sort((left, right) => left.id.localeCompare(right.id, "en"));

const output = {
  schemaVersion: 1,
  generatedAt: `${records.map(record => record.lastVerified || "1970-01-01").sort().at(-1)}T00:00:00.000Z`,
  records
};
await mkdir(join(root, "generated"), { recursive: true });
await writeFile(join(root, "generated", "gamedb-v1.json"), `${JSON.stringify(output, null, 2)}\n`);
console.log(`Built ${records.length} records.`);
