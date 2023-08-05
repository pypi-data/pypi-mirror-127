import{_ as o,H as s,e as t,t as a,p as i,b as e,Y as r,Z as c,$ as n,a0 as d,c as h,d as l,r as p,n as m}from"./main-52900fef.js";import{a as g}from"./c.0a038163.js";import"./c.947882ec.js";import"./c.f76541ed.js";import"./c.23bdaa19.js";import"./c.354b5629.js";import"./c.c6dcf38e.js";import"./c.9f27b448.js";import"./c.2f18e38b.js";import"./c.5f53c652.js";import"./c.2a9839e1.js";import"./c.c6868c89.js";import"./c.aadc44ec.js";import"./c.232d3787.js";import"./c.a37a4d8d.js";import"./c.72175d3a.js";let u=o([m("hacs-custom-repositories-dialog")],(function(o,s){return{F:class extends s{constructor(...s){super(...s),o(this)}},d:[{kind:"field",decorators:[t()],key:"_error",value:void 0},{kind:"field",decorators:[a()],key:"_progress",value:()=>!1},{kind:"field",decorators:[a()],key:"_addRepositoryData",value:()=>({category:void 0,repository:void 0})},{kind:"method",key:"shouldUpdate",value:function(o){return o.has("narrow")||o.has("active")||o.has("_error")||o.has("_addRepositoryData")||o.has("_progress")||o.has("repositories")}},{kind:"method",key:"render",value:function(){var o,s;if(!this.active)return i``;const t=null===(o=this.repositories)||void 0===o?void 0:o.filter(o=>o.custom),a=[{type:"string",name:"repository"},{type:"select",name:"category",optional:!0,options:this.hacs.configuration.categories.map(o=>[o,this.hacs.localize("common."+o)])}];return i`
      <hacs-dialog
        .active=${this.active}
        .hass=${this.hass}
        .title=${this.hacs.localize("dialog_custom_repositories.title")}
        scrimClickAction
        escapeKeyAction
        maxWidth
      >
        <div class="content">
          <div class="list" ?narrow=${this.narrow}>
            ${null!==(s=this._error)&&void 0!==s&&s.message?i`<ha-alert alert-type="error" .rtl=${g(this.hass)}>
                  ${this._error.message}
                </ha-alert>`:""}
            ${null==t?void 0:t.filter(o=>this.hacs.configuration.categories.includes(o.category)).map(o=>i`<ha-settings-row
                  @click=${()=>this._showReopsitoryInfo(String(o.id))}
                >
                  ${this.narrow?"":i`<ha-svg-icon slot="prefix" .path=${e}></ha-svg-icon>`}
                  <span slot="heading">${o.name}</span>
                  <span slot="description">${o.full_name} (${o.category})</span>

                  <mwc-icon-button
                    @click=${s=>{s.stopPropagation(),this._removeRepository(o.id)}}
                  >
                    <ha-svg-icon class="delete" .path=${r}></ha-svg-icon>
                  </mwc-icon-button>
                </ha-settings-row>`)}
          </div>
          <ha-form
            ?narrow=${this.narrow}
            .data=${this._addRepositoryData}
            .schema=${a}
            .computeLabel=${o=>"category"===o.name?this.hacs.localize("dialog_custom_repositories.category"):this.hacs.localize("common.repository")}
            @value-changed=${this._valueChanged}
          >
          </ha-form>
        </div>
        <mwc-button
          slot="primaryaction"
          raised
          .disabled=${void 0===this._addRepositoryData.category||void 0===this._addRepositoryData.repository}
          @click=${this._addRepository}
        >
          ${this._progress?i`<ha-circular-progress active size="small"></ha-circular-progress>`:this.hacs.localize("common.add")}
        </mwc-button>
      </hacs-dialog>
    `}},{kind:"method",key:"firstUpdated",value:function(){this.hass.connection.subscribeEvents(o=>this._error=o.data,"hacs/error")}},{kind:"method",key:"_valueChanged",value:function(o){this._addRepositoryData=o.detail.value}},{kind:"method",key:"_addRepository",value:async function(){this._error=void 0,this._progress=!0,this._addRepositoryData.category?this._addRepositoryData.repository?(await c(this.hass,this._addRepositoryData.repository,this._addRepositoryData.category),this.repositories=await n(this.hass),this._progress=!1):this._error={message:this.hacs.localize("dialog_custom_repositories.no_repository")}:this._error={message:this.hacs.localize("dialog_custom_repositories.no_category")}}},{kind:"method",key:"_removeRepository",value:async function(o){this._error=void 0,await d(this.hass,o),this.repositories=await n(this.hass)}},{kind:"method",key:"_showReopsitoryInfo",value:async function(o){this.dispatchEvent(new CustomEvent("hacs-dialog-secondary",{detail:{type:"repository-info",repository:o},bubbles:!0,composed:!0}))}},{kind:"get",static:!0,key:"styles",value:function(){return[h,l,p`
        .list {
          position: relative;
          max-height: calc(100vh - 500px);
          overflow: auto;
        }
        ha-form {
          display: block;
          padding: 25px 0;
        }
        ha-form[narrow] {
          background-color: var(--card-background-color);
          bottom: 0;
          position: absolute;
          width: calc(100% - 48px);
        }
        ha-svg-icon {
          --mdc-icon-size: 36px;
        }
        ha-svg-icon:not(.delete) {
          margin-right: 4px;
        }
        ha-settings-row {
          cursor: pointer;
          padding: 0;
        }
        .list[narrow] > ha-settings-row:last-of-type {
          margin-bottom: 162px;
        }
        .delete {
          color: var(--hcv-color-error);
        }

        @media all and (max-width: 450px), all and (max-height: 500px) {
          .list {
            max-height: calc(100vh - 162px);
          }
        }
      `]}}]}}),s);export{u as HacsCustomRepositoriesDialog};
