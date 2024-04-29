<script lang="ts">
  /*
    Docs:

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/MobileWorkMachine/StraddleCarrier/OperationsData_v0.1

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/MobileWorkMachine/StraddleCarrier/OperationsData_v0.1.py

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_MobileWorkMachine_StraddleCarrier_OperationsData_v0_1_DigitalProductPassport_MobileWorkMachine_StraddleCarrier_OperationsData_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"

  export let status: number
  export let data: {
    distance: number
    electricityUse: number
    fuelUse: number
  }
</script>

<Article>
  <DataRow label="Cumulative fuel use" value={formatNumber(data.fuelUse, "l")} />
  <DataRow label="Cumulative electricity use" value={formatNumber(data.electricityUse, "kWh")} />
  <DataRow label="Total distance" value={formatNumber(data.distance, "km")} />
</Article>
