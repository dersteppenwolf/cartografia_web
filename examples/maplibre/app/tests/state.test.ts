import { describe, expect, it } from "vitest";
import { readStateFromUrl } from "../src/state";

describe("readStateFromUrl", () => {
  it("uses the shared map state from a query string", () => {
    expect(readStateFromUrl("?lng=-74.1&lat=4.7&zoom=12&min=18")).toEqual({
      longitude: -74.1,
      latitude: 4.7,
      zoom: 12,
      minimumValue: 18,
    });
  });

  it("falls back to the course view for invalid values", () => {
    expect(readStateFromUrl("?lng=nope&min=")).toEqual({
      longitude: -74.07,
      latitude: 4.72,
      zoom: 11,
      minimumValue: null,
    });
  });
});
