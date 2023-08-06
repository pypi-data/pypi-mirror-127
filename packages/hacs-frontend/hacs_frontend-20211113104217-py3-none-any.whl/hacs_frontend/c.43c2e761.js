import{_ as o,H as t,e as s,t as i,p as a,Y as e,Z as r,$ as c,a0 as d,c as n,d as h,r as l,n as p}from"./main-01106cc7.js";import{a as m}from"./c.0a038163.js";import"./c.9f95d98f.js";import"./c.d44e03d8.js";import"./c.c35b4c87.js";import"./c.3ef6206b.js";import"./c.e7b1f016.js";import"./c.9f27b448.js";import"./c.38bc66f5.js";import"./c.fec508bb.js";import"./c.31517f43.js";import"./c.db9a58dd.js";import"./c.111028d2.js";import"./c.f1eb7adb.js";import"./c.301903e4.js";import"./c.f1b03c97.js";let u=o([p("hacs-custom-repositories-dialog")],(function(o,t){return{F:class extends t{constructor(...t){super(...t),o(this)}},d:[{kind:"field",decorators:[s()],key:"_error",value:void 0},{kind:"field",decorators:[i()],key:"_progress",value:()=>!1},{kind:"field",decorators:[i()],key:"_addRepositoryData",value:()=>({category:void 0,repository:void 0})},{kind:"method",key:"shouldUpdate",value:function(o){return o.has("narrow")||o.has("active")||o.has("_error")||o.has("_addRepositoryData")||o.has("_progress")||o.has("repositories")}},{kind:"method",key:"render",value:function(){var o,t;if(!this.active)return a``;const s=null===(o=this.hacs.repositories)||void 0===o?void 0:o.filter(o=>o.custom),i=[{type:"string",name:"repository"},{type:"select",name:"category",optional:!0,options:this.hacs.configuration.categories.map(o=>[o,this.hacs.localize("common."+o)])}];return a`
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
            ${null!==(t=this._error)&&void 0!==t&&t.message?a`<ha-alert alert-type="error" .rtl=${m(this.hass)}>
                  ${this._error.message}
                </ha-alert>`:""}
            ${null==s?void 0:s.filter(o=>this.hacs.configuration.categories.includes(o.category)).map(o=>a`<ha-settings-row
                  @click=${()=>this._showReopsitoryInfo(String(o.id))}
                >
                  <span slot="heading">${o.name}</span>
                  <span slot="description">${o.full_name} (${o.category})</span>

                  <mwc-icon-button
                    @click=${t=>{t.stopPropagation(),this._removeRepository(o.id)}}
                  >
                    <ha-svg-icon class="delete" .path=${e}></ha-svg-icon>
                  </mwc-icon-button>
                </ha-settings-row>`)}
          </div>
          <ha-form
            ?narrow=${this.narrow}
            .data=${this._addRepositoryData}
            .schema=${i}
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
          ${this._progress?a`<ha-circular-progress active size="small"></ha-circular-progress>`:this.hacs.localize("common.add")}
        </mwc-button>
      </hacs-dialog>
    `}},{kind:"method",key:"firstUpdated",value:function(){this.hass.connection.subscribeEvents(o=>this._error=o.data,"hacs/error")}},{kind:"method",key:"_valueChanged",value:function(o){this._addRepositoryData=o.detail.value}},{kind:"method",key:"_addRepository",value:async function(){if(this._error=void 0,this._progress=!0,!this._addRepositoryData.category)return void(this._error={message:this.hacs.localize("dialog_custom_repositories.no_category")});if(!this._addRepositoryData.repository)return void(this._error={message:this.hacs.localize("dialog_custom_repositories.no_repository")});await r(this.hass,this._addRepositoryData.repository,this._addRepositoryData.category);const o=await c(this.hass);this.dispatchEvent(new CustomEvent("update-hacs",{detail:{repositories:o},bubbles:!0,composed:!0})),this._progress=!1}},{kind:"method",key:"_removeRepository",value:async function(o){this._error=void 0,await d(this.hass,o);const t=await c(this.hass);this.dispatchEvent(new CustomEvent("update-hacs",{detail:{repositories:t},bubbles:!0,composed:!0}))}},{kind:"method",key:"_showReopsitoryInfo",value:async function(o){this.dispatchEvent(new CustomEvent("hacs-dialog-secondary",{detail:{type:"repository-info",repository:o},bubbles:!0,composed:!0}))}},{kind:"get",static:!0,key:"styles",value:function(){return[n,h,l`
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
      `]}}]}}),t);export{u as HacsCustomRepositoriesDialog};
