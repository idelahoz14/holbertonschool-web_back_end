export default class Currency {
    constructor(code, name) {
        if (typeof code !== 'string') throw TypeError('Code must be a String');
        if (typeof name !== 'string') throw TypeError('Name must be a String');
        this._code = code;
        this._name = name;
    }

    set code(code) {
        if (typeof code !== 'string') throw TypeError('Code must be a String');
        this._code = code;
    }

    get code() {
        return this._code;
    }

    set name(name) {
        if (typeof name !== 'string') throw TypeError('Name must be a String');
        this._code = code;
    }

    get name() {
        return this._code;
    }

    displayFullCurrency() {
        return '${this._name} (${this._code})';
    }
}
