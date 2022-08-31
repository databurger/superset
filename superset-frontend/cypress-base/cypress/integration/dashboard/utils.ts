/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

export function setGridMode(type: 'card' | 'list') {
    cy.get(`[aria-label="${type}-view"]`).click();
}

export function interceptFiltering() {
    cy.intercept('GET', `/api/v1/dashboard/?q=*`).as('filtering');
}

export function interceptBulkDelete() {
    cy.intercept('DELETE', `/api/v1/dashboard/?q=*`).as('bulkDelete');
}

export function interceptDelete() {
    cy.intercept('DELETE', `/api/v1/dashboard/*`).as('delete');
}

export function interceptUpdate() {
    cy.intercept('PUT', `/api/v1/dashboard/*`).as('update');
}

export function setFilter(filter: string, option: string) {
    interceptFiltering();

    cy.get(`[aria-label="${filter}"]`).first().click();
    cy.get(`[aria-label="${filter}"] [title="${option}"]`).click();

    cy.wait('@filtering');
}